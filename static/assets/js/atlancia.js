/* Atlancia: colour mode, reading progress and image zoom. */
(function () {
  'use strict';

  /* ------------------------------------------------------------------ */
  /* Colour mode. Follows the system until the reader chooses otherwise. */
  /* ------------------------------------------------------------------ */

  var MODES = ['auto', 'light', 'dark'];
  var LABELS = {
    auto: 'follow the system',
    light: 'light',
    dark: 'dark'
  };
  var STORAGE_KEY = 'atlancia-colour-mode';
  var root = document.documentElement;
  var toggle = document.querySelector('.js-theme-toggle');

  function readStored() {
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      return stored === 'light' || stored === 'dark' ? stored : null;
    } catch (error) {
      return null;
    }
  }

  function store(mode) {
    try {
      if (mode === 'auto') {
        localStorage.removeItem(STORAGE_KEY);
      } else {
        localStorage.setItem(STORAGE_KEY, mode);
      }
    } catch (error) {}
  }

  function systemMode() {
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  function apply(mode) {
    var resolved = mode === 'auto' ? systemMode() : mode;
    root.setAttribute('data-theme', resolved);
    store(mode);
    if (toggle) {
      toggle.setAttribute('data-mode', mode);
      var label = 'Colour mode: ' + LABELS[mode] + '. Click to change.';
      toggle.setAttribute('aria-label', label);
      toggle.setAttribute('title', label);
    }
  }

  if (toggle) {
    var mode = readStored() || 'auto';
    apply(mode);
    toggle.addEventListener('click', function () {
      mode = MODES[(MODES.indexOf(mode) + 1) % MODES.length];
      apply(mode);
    });
    /* While the reader has not chosen, follow the system as it changes. */
    var preference = window.matchMedia('(prefers-color-scheme: light)');
    var follow = function () {
      if (!readStored()) {
        apply('auto');
      }
    };
    if (preference.addEventListener) {
      preference.addEventListener('change', follow);
    } else if (preference.addListener) {
      preference.addListener(follow);
    }
  }

  /* ------------------------------------------------------------------ */
  /* How far through the essay the reader is. */
  /* ------------------------------------------------------------------ */

  var bar = document.querySelector('.progress__bar');
  if (bar) {
    var updateProgress = function () {
      var height = document.documentElement.scrollHeight - window.innerHeight;
      var done = height > 0 ? Math.min(1, window.scrollY / height) : 0;
      bar.style.transform = 'scaleX(' + done + ')';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);
    updateProgress();
  }

  /* ------------------------------------------------------------------ */
  /* Open an image larger when it is clicked. */
  /* ------------------------------------------------------------------ */

  var overlay = document.getElementById('zoom');
  if (overlay) {
    var large = overlay.querySelector('.zoom__image');
    var close = overlay.querySelector('.zoom__close');

    var open = function (image) {
      large.src = image.currentSrc || image.src;
      large.alt = image.alt || '';
      overlay.hidden = false;
      document.body.style.overflow = 'hidden';
    };

    var shut = function () {
      overlay.hidden = true;
      large.removeAttribute('src');
      document.body.style.overflow = '';
    };

    var images = document.querySelectorAll('.content__entry img, .atlx img');
    Array.prototype.forEach.call(images, function (image) {
      image.addEventListener('click', function () {
        open(image);
      });
    });

    close.addEventListener('click', shut);
    overlay.addEventListener('click', function (event) {
      if (event.target === overlay) {
        shut();
      }
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !overlay.hidden) {
        shut();
      }
    });
  }
})();
