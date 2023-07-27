function display_student_grade() {
    var fullName = document.getElementById("full-name").value;
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "https://amhep.pythonanywhere.com/grades/";
    const async = true;
    xhttp.open(method, url + fullName, async);
    xhttp.send();
    xhttp.onload = function() {
        document.getElementById("display-student-grade").innerHTML = this.responseText;
    };
}

function create_new_entry() {
    var fullName = document.getElementById("full_name").value;
    var grade = document.getElementById("grade").value;
    var xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades";    
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"name": fullName, "grade": Number(grade)};
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == fullName) {
                document.getElementById("create-new-entry").innerHTML = key + ": " + value;
            }
        });
    };    
}

function edit_existing_grade() {
    var fullName = document.getElementById("full_n").value;
    var newGrade = document.getElementById("new_grade").value;
    var xhttp = new XMLHttpRequest();
    const method = "PUT";
    const url = "https://amhep.pythonanywhere.com/grades/";
    const async = true;
    xhttp.open(method, url + fullName, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"name": fullName, "grade": Number(newGrade)};
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == fullName) {
                document.getElementById("edit-existing-grade").innerHTML = key + ": " + value;
            }
        });
    };
}

function delete_entry() {
    var fullName = document.getElementById("full_na").value;
    var num = 0;
    var xhttp = new XMLHttpRequest();
    const method = "DELETE";
    const url = "https://amhep.pythonanywhere.com/grades/";
    const async = true;
    xhttp.open(method, url + fullName, async);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send();
    xhttp.onload = function() {
        let data = this.responseText;
        data = JSON.parse(data);
        Object.entries(data).forEach(([key, value]) => {
            if (key == fullName) {
                num++;
            }
        });
        if(num == 0) {
            document.getElementById("deleted-entry").innerHTML = this.responseText;
        }
    };
}

function all_grades() {
    const xhttp = new XMLHttpRequest();
    const method = "GET";
    const url = "https://amhep.pythonanywhere.com/grades";
    const async = true;
    xhttp.open(method, url, async);
    xhttp.send();
    xhttp.onload = function() {
        document.getElementById("all-grades").innerHTML = this.responseText;
    }
}