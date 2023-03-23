const toastElement = document.getElementById("toast");

function removeToast() {
  toastElement.remove();
}

export function checkToastPresence() {
  if (toastElement) {
    const closeBtn = toastElement.lastElementChild;
    setTimeout(removeToast, 5000);

    closeBtn.addEventListener("click", removeToast);
  }
}
