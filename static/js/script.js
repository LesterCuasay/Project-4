// Function for copyright date

function currentYear() {

    let fullYear = new Date();
    let yearNow = fullYear.getFullYear();

    document.getElementById("year").innerHTML = yearNow;
}

currentYear();

// Event listener for ratings field

document.addEventListener('DOMContentLoaded', function () {
    let starRatings = document.querySelectorAll('.rating-star')

    starRatings.forEach(function(star) {
        star.addEventListener('click', function () {
            let starValue = this.getAttribute('data-value');
            let fieldName = this.getAttribute('data-name');
            let hiddenInput = document.querySelector('input[name="' + fieldName + '"]');
            if (hiddenInput) {
                hiddenInput.value = starValue;
            }
            console.log('Clicked star: value= ' + starValue + 'name= ' + fieldName);
        });

        star.addEventListener('mouseover', function() {
            let hoverStarValue = this.getAttribute('data-value');
            let stars = Array.from(this.parentNode.children);

            stars.forEach(function(star) {
                let starValue = star.getAttribute('data-value');
                star.classList.toggle('checked', starValue <= hoverStarValue);
            });
        });
    })
})