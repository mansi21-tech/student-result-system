// ---------------- ADD RESULT VALIDATION ----------------

function validateForm() {

    let name =
        document.getElementById("name").value.trim();

    let roll =
        document.getElementById("roll_no").value.trim();


    let maths =
        Number(document.getElementById("maths").value);

    let science =
        Number(document.getElementById("science").value);

    let english =
        Number(document.getElementById("english").value);

    let computer =
        Number(document.getElementById("computer").value);


    if (roll === "") {

        alert("Please enter roll number.");

        return false;
    }


    if (name === "") {

        alert("Please enter student name.");

        return false;
    }


    if (
        maths < 0 || maths > 100 ||
        science < 0 || science > 100 ||
        english < 0 || english > 100 ||
        computer < 0 || computer > 100
    ) {

        alert("Marks must be between 0 and 100.");

        return false;
    }


    return true;
}


// ---------------- LIVE CALCULATION ----------------

function calculatePreview() {

    let maths =
        Number(document.getElementById("maths").value) || 0;

    let science =
        Number(document.getElementById("science").value) || 0;

    let english =
        Number(document.getElementById("english").value) || 0;

    let computer =
        Number(document.getElementById("computer").value) || 0;


    let total =
        maths + science + english + computer;


    let percentage =
        total / 4;


    let preview =
        document.getElementById("preview");


    preview.innerHTML =
        "Total: " +
        total +
        " | Percentage: " +
        percentage.toFixed(2) +
        "%";
}


// ---------------- SEARCH VALIDATION ----------------

function validateSearch() {

    let roll =
        document.getElementById("searchRoll").value.trim();


    if (roll === "") {

        alert("Please enter roll number.");

        return false;
    }


    return true;
}