const url1 = "http://127.0.0.1:5000/grades/";
const url2 = "http://127.0.0.1:5000/std/";
const url3 = "http://127.0.0.1:5000/teach/";
const url4 = "http://127.0.0.1:5000/classes/";


document.addEventListener('DOMContentLoaded', () => {
  // get all the buttons and student count elements
  const dropButtons = document.querySelectorAll('.drop-btn');
  const enrollButtons = document.querySelectorAll('.enroll-btn');

  // Attach a click event listener to each drop button
  dropButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Check if the button has already been clicked
      if (button.classList.contains('disabled')) {
        return;
      }
      button.classList.add('disabled');
      button.innerText = 'Dropped';
      const studentCount = button.parentElement.previousElementSibling;
      const [enrolled, capacity] = studentCount.innerText.split('/');
      studentCount.innerText = `${parseInt(enrolled) - 1}/${capacity}`;

      // Check if the corresponding enroll button is disabled
      const enrollButton = button.nextElementSibling;
      if (enrollButton.classList.contains('disabled')) {
        enrollButton.classList.remove('disabled');
        enrollButton.innerText = 'Enroll';
      }
    });
  });

  // Attach a click event listener to each enroll button
  enrollButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Check if the button has already been clicked
      if (button.classList.contains('disabled')) {
        return;
      }
      button.classList.add('disabled');
      button.innerText = 'Enrolled';
      const studentCount = button.parentElement.previousElementSibling;
      const [enrolled, capacity] = studentCount.innerText.split('/');
      studentCount.innerText = `${parseInt(enrolled) + 1}/${capacity}`;

      // Check if the corresponding drop button is disabled
      const dropButton = button.previousElementSibling;
      if (dropButton.classList.contains('disabled')) {
        dropButton.classList.remove('disabled');
        dropButton.innerText = 'Drop';
      }
    });
  });
});

window.onload = function() {
  startTab();
};

function startTab() {
  document.getElementById("default").click();

}

//Nevin did this portion
function openTab(evt, Tab) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(Tab).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("default").click();

//Nevin did this portion
function delete_student() {

  let count = 0;
  const name3 = document.getElementById("nom").value;

  const req = new XMLHttpRequest();
  const method = "DELETE";

  req.open(method, url2 + name3);
  req.setRequestHeader("Content-Type", "application/json");

  req.send();
}

//Nevin did this portion
function delete_teacher() {

  let count = 0;
  const name3 = document.getElementById("dname").value;

  const req = new XMLHttpRequest();
  const method = "DELETE";

  req.open(method, url3 + name3);
  req.setRequestHeader("Content-Type", "application/json");

  req.send();
}

//Nevin did this portion
function delete_class() {

  let count = 0;
  const name3 = document.getElementById("dnom").value;

  const req = new XMLHttpRequest();
  const method = "DELETE";

  req.open(method, url4 + name3);
  req.setRequestHeader("Content-Type", "application/json");

  req.send();
}

function changeTeach() {
  var ret = new XMLHttpRequest();
  var ctnom = document.getElementById("ctnom").value;
  var teach = document.getElementById("teach").value;
  ret.open("PUT", url4 + ctnom, true);
  ret.setRequestHeader("Content-Type", "application/json");
  const body = { "teach": String(teach) };
  ret.send(JSON.stringify(body));

}


function newStudent() {
    var req = new XMLHttpRequest();
    var student_username = document.getElementById("student_username").value;
    var student_password = document.getElementById("student_password").value;
    var student_name = document.getElementById("student_name").value;
    req.open("POST", url2, true);
    req.setRequestHeader("Content-Type", "application/json");
    const corpus = {"student_username": String(student_username), "student_password": String(student_password), "student_name": String(student_name)};
    req.send(JSON.stringify(corpus));
}


function newAdmin() {
    var req = new XMLHttpRequest();
    var admin_username = document.getElementById("admin_username").value;
    var admin_password = document.getElementById("admin_password").value;
    req.open("POST", "http://127.0.0.1:5000/admin/", true);
    req.setRequestHeader("Content-Type", "application/json");
    const body = {"admin_username": String(admin_username), "admin_password": String(admin_password)};
    req.send(JSON.stringify(body));
}

function newTeachLogin() {
    var req = new XMLHttpRequest();
    var teacher_username = document.getElementById("teacher_username").value;
    var teacher_password = document.getElementById("teacher_password").value;
    var new_teacher_name = document.getElementById("new_teacher_name").value;
    req.open("POST", url3, true);
    req.setRequestHeader("Content-Type", "application/json");
    const corpus = {"teacher_username": String(teacher_username), "teacher_password": String(teacher_password), "new_teacher_name": String(new_teacher_name)};
    req.send(JSON.stringify(corpus));
}

function newClass() {
    var req = new XMLHttpRequest();
    var class_name = document.getElementById("class_name").value;
    var class_teacher = document.getElementById("class_teacher").value;
    req.open("POST", url4, true);
    req.setRequestHeader("Content-Type", "application/json");
    const body = {"class_name": String(class_name), "class_teacher": String(class_teacher)};
    req.send(JSON.stringify(body));
 }

 function addStudentClass() {
    var req = new XMLHttpRequest();
    var cnaam = document.getElementById("cnaam").value;
    var nsname = document.getElementById("nsname").value;
    req.open("POST", url1, true);
    req.setRequestHeader("Content-Type", "application/json");
    const body = {"cnaam": String(cnaam), "nsname": String(nsname)};
    req.send(JSON.stringify(body));
 }

function changeGrad() {
    var ret = new XMLHttpRequest();
    var snam = document.getElementById("snam").value;
    var cgradename = document.getElementById("cgradename").value;
    var newgrae = document.getElementById("newgrae").value;

    ret.open("PUT", url1 + snam, true);
    ret.setRequestHeader("Content-Type", "application/json");
    const body = { "cgradename": String(cgradename), "newgrae" : (newgrae)};
    ret.send(JSON.stringify(body));

}
//This is what Richard and Wendy did, drop and enroll are for students who want to drop/enroll given within their class
function drop(class_name, user_name) {
    const req = new XMLHttpRequest();
    req.open("DELETE", "http://127.0.0.1:5000/drop/" + class_name + "/" + user_name);
    req.setRequestHeader("Content-Type", "application/json");
    req.send();
}
//Richard did this portion
function enroll(user_name, class_name){
    const req = new XMLHttpRequest();
    req.open("POST", "http://127.0.0.1:5000/enroll/" + user_name + "/" + class_name);
    req.setRequestHeader("Content-Type", "application/json");
    req.send();
}

function update(class_name, Name, grade_id){
  const req = new XMLHttpRequest();
  const grade = document.getElementById(grade_id).value;
  req.open("PUT", "http://127.0.0.1:5000/update/" + class_name+ "/" + Name);
  req.setRequestHeader("Content-Type", "application/json");
  const body = {"grade": grade}
  req.send(JSON.stringify(body));
}
