/* Zone Zero Orange County — site.js
   Form -> shared Make.com network scenario 5600808 webhook.
   reCAPTCHA v3 token attached client-side; verified server-side in Make.
   event_id shared with Meta Pixel Lead event for CAPI deduplication. */
(function () {
  'use strict';

  var WEBHOOK_URL = 'https://hook.us2.make.com/mi0lks6grssbjq9hopp9pd0tdudexfgo';
  var SITE = 'zonezeroventura.com';
  var RECAPTCHA_SITE_KEY = '6Lfh4U4tAAAAALuYKhSwIpggriOhdKqEsj6XBFo6';

  /* Nav toggle */
  var toggle = document.querySelector('.zz-nav-toggle');
  var links = document.querySelector('.zz-nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('zz-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  function makeEventId() {
    return 'zz-' + Date.now() + '-' + Math.random().toString(36).slice(2, 10);
  }

  function getRecaptchaToken() {
    return new Promise(function (resolve) {
      if (!window.grecaptcha || !window.grecaptcha.execute) { resolve(''); return; }
      window.grecaptcha.ready(function () {
        window.grecaptcha.execute(RECAPTCHA_SITE_KEY, { action: 'lead' })
          .then(resolve)
          .catch(function () { resolve(''); });
      });
    });
  }

  var form = document.querySelector('.zz-form[data-webhook]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"]');
      var status = form.querySelector('.zz-form-status');
      var payload = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.name && el.name !== 'consent') { payload[el.name] = el.value; }
      });
      payload._site = SITE;
      payload._page = window.location.pathname;
      payload._event_id = makeEventId();

      if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
      payload.consent = true;
      payload.consent_text_version = 'zz-consent-v1-2026-08-21';
      payload.consent_ts = new Date().toISOString();
      payload.consent_page_url = location.href;
      payload.form_id = form.id || 'zz-find-contractor';


      getRecaptchaToken().then(function (token) {
        payload._recaptcha_token = token;
        return fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }).then(function (res) {
        if (!res.ok) { throw new Error('bad status'); }
        if (typeof fbq === 'function') {
          fbq('track', 'Lead', {}, { eventID: payload._event_id });
        }
        if (typeof gtag === 'function') {
          gtag('event', 'generate_lead', { event_id: payload._event_id });
        }
        form.reset();
        if (status) {
          status.style.display = 'block';
          status.style.color = '#33502E';
          status.textContent = 'Thank you. We\'ll review your property and contact you within one business day to talk through your Zone 0 options and, if you\'d like, connect you with an independent CSLB-licensed contractor.';
        }
        if (btn) { btn.textContent = 'Request sent'; }
      }).catch(function () {
        if (status) {
          status.style.display = 'block';
          status.style.color = '#BF0A30';
          status.textContent = 'Something went wrong sending your request. Please try again, or call (805) 567-8416.';
        }
        if (btn) { btn.disabled = false; btn.textContent = 'Request my free assessment'; }
      });
    });
  }
})();
