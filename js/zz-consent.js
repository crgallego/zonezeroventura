/* Zone Zero analytics and ads consent. On by default. Off when the browser sends
   Global Privacy Control or the visitor chose "off". Loads GA4 and the Meta pixel only when on.
   Form pages send no PageView; the only pixel event there is Lead, fired by site.js on submit. */
(function () {
  'use strict';

  var ga = metaContent('zz-ga4');
  var pixels = metaContent('zz-pixel').split(',').filter(Boolean);
  var storageKey = 'zz-privacy-choice-v1';
  var gpc = navigator.globalPrivacyControl === true;
  var formPage = !!document.querySelector('form.zz-form');
  var gaLoaded = false;
  var pixelLoaded = false;

  function metaContent(name) {
    var el = document.querySelector('meta[name="' + name + '"]');
    return el ? el.getAttribute('content') : '';
  }
  function readChoice() {
    try { return window.localStorage.getItem(storageKey); } catch (e) { return null; }
  }
  function saveChoice(value) {
    try { window.localStorage.setItem(storageKey, value); } catch (e) {}
  }

  function loadGA() {
    if (!ga || gaLoaded) return;
    gaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ga);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ga;
    document.head.appendChild(s);
  }

  function loadPixel() {
    if (!pixels.length || pixelLoaded) return;
    pixelLoaded = true;
    /* Meta's standard base code. */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n;
      n.push = n; n.loaded = true; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = true; t.src = v;
      s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    pixels.forEach(function (id) { window.fbq('init', id); });
    if (!formPage) window.fbq('track', 'PageView');
  }

  var on = !gpc && readChoice() !== 'denied';

  function apply(next) {
    on = next;
    if (ga) window['ga-disable-' + ga] = !on;
    if (on) {
      loadGA();
      loadPixel();
      if (window.fbq) window.fbq('consent', 'grant');
    } else if (window.fbq) {
      window.fbq('consent', 'revoke');
    }
  }
  apply(on);

  window.zzConsent = { state: function () { return on ? 'granted' : 'denied'; } };

  /* Footer "Privacy choices" link and a small panel. */
  var style = document.createElement('style');
  style.textContent =
    '.zz-pc-link{background:none;border:0;padding:0;margin:8px 0 0;color:inherit;font:inherit;text-decoration:underline;cursor:pointer;display:block}' +
    '.zz-pc-panel{position:fixed;z-index:2147483000;left:16px;bottom:16px;max-width:360px;padding:16px;background:#171717;color:#f4f1ea;border:1px solid rgba(244,241,234,.35);font:14px/1.5 system-ui,sans-serif;box-shadow:0 12px 40px rgba(0,0,0,.3)}' +
    '.zz-pc-panel[hidden]{display:none}' +
    '.zz-pc-panel p{margin:0 0 12px;color:#f4f1ea}' +
    '.zz-pc-panel a{color:#ffcc00}' +
    '.zz-pc-panel button{min-height:40px;padding:8px 14px;margin-right:8px;background:#ffcc00;color:#171717;border:1px solid #ffcc00;font:600 13px system-ui,sans-serif;cursor:pointer}' +
    '.zz-pc-panel button.zz-pc-close{background:transparent;color:#f4f1ea;border-color:rgba(244,241,234,.5)}' +
    '.zz-pc-panel button:focus-visible,.zz-pc-link:focus-visible{outline:3px solid #fff;outline-offset:3px}';
  document.head.appendChild(style);

  var panel = document.createElement('section');
  panel.className = 'zz-pc-panel';
  panel.id = 'privacy-choices';
  panel.hidden = true;
  panel.setAttribute('role', 'region');
  panel.setAttribute('aria-label', 'Privacy choices');
  panel.innerHTML =
    '<p class="zz-pc-status"></p>' +
    '<p><a href="/privacy/">Read the Privacy Policy</a></p>' +
    '<button type="button" class="zz-pc-toggle"></button>' +
    '<button type="button" class="zz-pc-close">Close</button>';
  var status = panel.querySelector('.zz-pc-status');
  var toggle = panel.querySelector('.zz-pc-toggle');

  function render() {
    if (gpc) {
      status.textContent = 'Browser privacy signal honored. Analytics and ads measurement are off.';
      toggle.hidden = true;
    } else if (on) {
      status.textContent = 'Analytics and ads measurement are on. You can turn them off at any time.';
      toggle.textContent = 'Turn off analytics and ads';
    } else {
      status.textContent = 'Analytics and ads measurement are off. You can turn them on at any time.';
      toggle.textContent = 'Turn on analytics and ads';
    }
  }
  render();

  var link = document.createElement('button');
  link.type = 'button';
  link.className = 'zz-pc-link';
  link.textContent = 'Privacy choices';
  link.setAttribute('aria-controls', 'privacy-choices');
  link.setAttribute('aria-expanded', 'false');

  function show(open) {
    panel.hidden = !open;
    link.setAttribute('aria-expanded', String(open));
  }
  link.addEventListener('click', function () { show(panel.hidden); });
  panel.querySelector('.zz-pc-close').addEventListener('click', function () { show(false); });
  toggle.addEventListener('click', function () {
    if (gpc) return;
    var next = !on;
    saveChoice(next ? 'granted' : 'denied');
    apply(next);
    render();
  });

  var host = document.querySelector('footer .zz-footer-bottom') || document.querySelector('footer') || document.body;
  host.appendChild(link);
  document.body.appendChild(panel);
})();
