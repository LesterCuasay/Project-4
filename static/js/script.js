/** Function for copyright date  */

function currentYear() {

    let fullYear = new Date();
    let yearNow = fullYear.getFullYear();

    document.getElementById("year").innerHTML = yearNow;
}

currentYear();


document.addEventListener('DOMContentLoaded', function () {
    let starRatings = document.querySelectorAll('.rating-star')

    starRatings.forEach(function (star) {
        star.addEventListener('click', function () {
            let starValue = this.getAttribute('data-value');
            let fieldName = this.getAttribute('data-name');
            document.querySelector('input[name="' + fieldName + '"]').value = starValue;
        })
    })
})