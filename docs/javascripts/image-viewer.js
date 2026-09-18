/* Progressive enhancement: screenshot links still open the original without JS. */
document.addEventListener("DOMContentLoaded", () => {
  const dialog = document.createElement("dialog");
  dialog.className = "lab-image-dialog";
  dialog.setAttribute("aria-label", "Enlarged lab screenshot");
  const close = document.createElement("button");
  close.type = "button";
  close.textContent = "Close ×";
  const image = document.createElement("img");
  dialog.append(close, image);
  document.body.append(dialog);
  close.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", event => {
    if (event.target === dialog) dialog.close();
  });
  document.querySelectorAll(".md-content img.lab-screenshot").forEach(img => {
    if (img.closest("a")) return;
    const link = document.createElement("a");
    link.href = img.src;
    link.className = "image-zoom";
    link.setAttribute("aria-label", `Enlarge: ${img.alt}`);
    img.replaceWith(link);
    link.append(img);
    link.addEventListener("click", event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || !dialog.showModal) return;
      event.preventDefault();
      image.src = img.src;
      image.alt = img.alt;
      dialog.showModal();
    });
  });
});
