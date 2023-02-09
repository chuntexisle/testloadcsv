// https://docs.djangoproject.com/en/3.2/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function getAllTodos(url) {
  $.ajax({
    url: url,
    type: "GET",
    dataType: "json",
    success: (data) => {
      const todoList = $("#todoList");
      todoList.empty();

      (data.context).forEach(todo => {
        const todoHTMLElement = `
          <li>
            <p>Task: ${todo.task}</p>
            <p>Completed?: ${todo.completed}</p>
          </li>`
        todoList.append(todoHTMLElement);
      });
    },
    error: (error) => {
      console.log(error);
    }
  });
}
