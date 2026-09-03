(() => {
  const UG_TUITION = 12072;
  const dialog = document.getElementById("lead-inquiry-dialog");
  const leadForm = document.getElementById("lead-form");
  const leadSuccess = document.getElementById("lead-success");
  const mobileNav = document.getElementById("mobile-nav");
  const mobileToggle = document.querySelector("[data-mobile-toggle]");

  const money = (n) =>
    n.toLocaleString("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });

  function setPersona(key) {
    document.querySelectorAll("[data-persona]").forEach((tab) => {
      const on = tab.getAttribute("data-persona") === key;
      tab.classList.toggle("active", on);
      tab.setAttribute("aria-selected", String(on));
    });
    document.querySelectorAll("[data-persona-panel]").forEach((panel) => {
      const on = panel.getAttribute("data-persona-panel") === key;
      panel.classList.toggle("active", on);
      panel.hidden = !on;
    });
  }

  function setCalc(key) {
    document.querySelectorAll("[data-calc]").forEach((tab) => {
      const on = tab.getAttribute("data-calc") === key;
      tab.classList.toggle("active", on);
      tab.setAttribute("aria-selected", String(on));
    });
    document.querySelectorAll("[data-calc-panel]").forEach((panel) => {
      const on = panel.getAttribute("data-calc-panel") === key;
      panel.classList.toggle("active", on);
      panel.hidden = !on;
    });
  }

  function updateAidCalculator() {
    const boxes = document.querySelectorAll('#ug-aid-stack input[type="checkbox"]');
    let aid = 0;
    boxes.forEach((box) => {
      const row = box.closest(".aid-option-row");
      row.classList.toggle("checked", box.checked);
      if (box.checked) aid += Number(box.dataset.amount || 0);
    });
    const net = Math.max(0, UG_TUITION - aid);
    const surplus = Math.max(0, aid - UG_TUITION);
    const netEl = document.getElementById("ug-net");
    const subEl = document.getElementById("ug-net-sub");
    const aidEl = document.getElementById("ug-aid-total");
    const deltaEl = document.getElementById("ug-delta");
    if (!netEl) return;
    netEl.textContent = money(net);
    aidEl.textContent = money(aid);
    deltaEl.textContent = surplus > 0 ? `+${money(surplus)} surplus` : money(net);
    if (net === 0 && surplus > 0) {
      subEl.textContent = `Aid covers full KY resident tuition, with ${money(surplus)} left toward housing, meals, or books.`;
      netEl.style.color = "#34D399";
    } else if (net === 0) {
      subEl.textContent = "Estimated net tuition is $0 for this stack.";
      netEl.style.color = "#34D399";
    } else {
      subEl.textContent = "Add eligible awards or file the FAFSA to close the gap.";
      netEl.style.color = "#FBBF24";
    }
  }

  function openDialog() {
    if (!dialog) return;
    leadForm.hidden = false;
    leadSuccess.classList.remove("active");
    dialog.showModal();
    document.getElementById("lead-name")?.focus();
  }

  function closeDialog() {
    dialog?.close();
  }

  function toggleMobile(force) {
    if (!mobileNav || !mobileToggle) return;
    const open = typeof force === "boolean" ? force : mobileNav.hidden;
    mobileNav.hidden = !open;
    mobileNav.classList.toggle("open", open);
    mobileToggle.setAttribute("aria-expanded", String(open));
  }

  document.querySelectorAll("[data-persona]").forEach((tab) => {
    tab.addEventListener("click", () => setPersona(tab.getAttribute("data-persona")));
  });

  document.querySelectorAll("[data-calc]").forEach((tab) => {
    tab.addEventListener("click", () => setCalc(tab.getAttribute("data-calc")));
  });

  document.querySelectorAll('#ug-aid-stack input[type="checkbox"]').forEach((box) => {
    box.addEventListener("change", updateAidCalculator);
  });

  document.querySelectorAll("[data-open-dialog]").forEach((btn) => {
    btn.addEventListener("click", openDialog);
  });

  document.querySelectorAll("[data-close-dialog]").forEach((btn) => {
    btn.addEventListener("click", closeDialog);
  });

  dialog?.addEventListener("click", (event) => {
    if (event.target === dialog) closeDialog();
  });

  leadForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(leadForm).entries());
    try {
      const existing = JSON.parse(sessionStorage.getItem("eled-leads") || "[]");
      existing.push({ ...data, at: new Date().toISOString(), program: "ELED-527" });
      sessionStorage.setItem("eled-leads", JSON.stringify(existing));
    } catch {
      /* demo storage is optional */
    }
    leadForm.hidden = true;
    leadSuccess.classList.add("active");
  });

  mobileToggle?.addEventListener("click", () => toggleMobile());
  mobileNav?.querySelectorAll("a, button").forEach((el) => {
    el.addEventListener("click", () => toggleMobile(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") toggleMobile(false);
  });

  updateAidCalculator();
})();
