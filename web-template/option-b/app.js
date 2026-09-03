(() => {
  const sms = (body) =>
    `sms:+12707218539?body=${encodeURIComponent(body)}`;

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const id = link.getAttribute("href").slice(1);
      const target = document.getElementById(id);
      const scroller = document.querySelector(".scroll");
      if (!target || !scroller) return;
      event.preventDefault();
      scroller.scrollTo({ top: target.offsetTop, behavior: "smooth" });
    });
  });

  document.querySelectorAll("[data-sms]").forEach((btn) => {
    btn.addEventListener("click", () => {
      window.location.href = sms(btn.getAttribute("data-sms"));
    });
  });

  function exclusive(group, attr, key) {
    document.querySelectorAll(`[${attr}]`).forEach((btn) => {
      const on = btn.getAttribute(attr) === key;
      btn.setAttribute("aria-pressed", String(on));
    });
    document.querySelectorAll(`[${attr}-panel]`).forEach((panel) => {
      panel.classList.toggle("on", panel.getAttribute(`${attr}-panel`) === key);
    });
  }

  document.querySelectorAll("[data-geo]").forEach((btn) => {
    btn.addEventListener("click", () => exclusive("geo", "data-geo", btn.getAttribute("data-geo")));
  });

  document.querySelectorAll("[data-who]").forEach((btn) => {
    btn.addEventListener("click", () => exclusive("who", "data-who", btn.getAttribute("data-who")));
  });

  const tip = document.getElementById("aid-tip");
  document.querySelectorAll(".layer").forEach((layer) => {
    layer.addEventListener("click", () => {
      if (tip) tip.textContent = layer.getAttribute("data-tip") || "";
    });
  });

  const sheet = document.getElementById("ask");
  const back = document.querySelector(".sheet-back");
  const formWrap = document.getElementById("ask-form-wrap");
  const thanks = document.getElementById("ask-thanks");

  function openSheet() {
    sheet.hidden = false;
    back.hidden = false;
    requestAnimationFrame(() => {
      sheet.classList.add("on");
      back.classList.add("on");
    });
    document.getElementById("n")?.focus();
  }

  function closeSheet() {
    sheet.classList.remove("on");
    back.classList.remove("on");
    window.setTimeout(() => {
      sheet.hidden = true;
      back.hidden = true;
    }, 200);
  }

  document.querySelectorAll("[data-open-sheet]").forEach((el) => el.addEventListener("click", openSheet));
  document.querySelectorAll("[data-close-sheet]").forEach((el) => el.addEventListener("click", closeSheet));
  back?.addEventListener("click", closeSheet);

  document.getElementById("ask-form")?.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(event.target).entries());
    try {
      sessionStorage.setItem(
        "eled-option-b-lead",
        JSON.stringify({ ...data, at: new Date().toISOString() })
      );
    } catch {
      /* demo only */
    }
    formWrap.hidden = true;
    thanks.classList.add("on");
  });
})();
