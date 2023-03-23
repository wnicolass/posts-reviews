const updatePostForm = document.getElementById("edit-post");

async function updatePost() {
  const { postId } = updatePostForm.dataset;
  const formData = new FormData(updatePostForm);
  let post;
  for (let [key, val] of formData) {
    post[key] = val;
  }

  try {
    const res = await fetch(`/posts/edit/${postId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ post }),
    });

    if (!res.ok) {
      alert("Something went wrong!");
      return;
    }
  } catch (err) {
    alert("Something went wrong!");
    return;
  }
}

if (updatePostForm) {
  updatePostForm.addEventListener("submit", (event) => {
    event.preventDefault();
    updatePost();
  });
}
