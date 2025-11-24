document.addEventListener("DOMContentLoaded", () => {
  const elements = {
    viewMode: document.getElementById("view-mode"),
    editMode: document.getElementById("edit-mode"),
    btnEdit: document.getElementById("btn-edit"),
    btnCancel: document.getElementById("btn-cancel"),
    avatarInput: document.querySelector('input[name="avatar_file"]'),
    avatarPreview: document.getElementById("avatar-preview"),
  };

  const toggleMode = (showEdit) => {
    elements.viewMode.style.display = showEdit ? "none" : "block";
    elements.editMode.style.display = showEdit ? "block" : "none";
  };

  elements.btnEdit?.addEventListener("click", () => toggleMode(true));
  elements.btnCancel?.addEventListener("click", () => toggleMode(false));

  elements.avatarInput?.addEventListener("change", (e) => {
    const file = e.target.files?.[0];
    if (file && elements.avatarPreview) {
      const reader = new FileReader();
      reader.onload = (event) => {
        elements.avatarPreview.src = event.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
});
