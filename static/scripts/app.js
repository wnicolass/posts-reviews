const toastElement = document.getElementById("toast");

function removeToast() {
  toastElement.remove();
}

function main() {
  if (toastElement) {
    const closeBtn = toastElement.lastElementChild;
    setTimeout(removeToast, 5000);

    closeBtn.addEventListener("click", removeToast);
  }
}

main();
