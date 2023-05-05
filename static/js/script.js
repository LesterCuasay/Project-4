function year() {

    let dateToday = new Date();

    let dateObject = dateToday.getFullYear();

    document.getElementById("year").innerHTML = dateObject;
}

year()