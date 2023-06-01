
/** Function for copyright date  */

function currentYear() {

    let fullYear = new Date ();
    let yearNow = fullYear.getFullYear();

    document.getElementById("year").innerHTML = yearNow;
}

currentYear();