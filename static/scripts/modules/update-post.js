const updatePostForm = document.getElementById("edit-post");

async function updatePost({ target: form }) {
  const { postid } = form.dataset;
  const formData = new FormData(form);
  let post = {
    title: formData.get("title"),
    summary: formData.get("summary"),
    content: formData.get("content"),
  };

  try {
    const res = await fetch(`/posts/edit/${postid}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...post }),
    });

    if (!res.ok) {
      alert("Something went wrong!");
      return;
    }

    window.location.replace("http://localhost:8000/posts");
  } catch (err) {
    alert("Something went wrong!");
    return;
  }
}

if (updatePostForm) {
  updatePostForm.addEventListener("submit", (event) => {
    event.preventDefault();
    updatePost(event);
  });
}
