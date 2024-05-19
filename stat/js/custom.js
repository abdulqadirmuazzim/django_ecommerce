// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// owl carousel 

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 6
        }
    }
})

window.addEventListener('scroll', () => {

    var top1 = document.querySelector('#topnav')
    var value = 0
    if (window.scrollY > value) {
        top1.classList.add("scrolled-up")
    } else {
        top1.classList.remove('scrolled-up')
    }
    window.scrollY = value

})

// search bar
document.addEventListener("DOMContentLoaded", function () {
    const searchBtn = document.querySelector(".nav_search-btn");
    const searchInput = document.querySelector(".form-inline");
    var find = document.querySelector("#search")
    var input = document.querySelector(".search-input")
    // When search Icon is clicked
    searchBtn.addEventListener("click", function () {
        // Toggle visibility of the search input when the button is clicked
        searchInput.style.display = (searchInput.style.display === "block") ? "none" : "block";
    });
    // when search buttton is clicked
    // find.addEventListener("click", function () {
    //   const query = input.value.trim(); // Get the search query from the input field
    //   if (query) {
    //     window.location.href = `/search/?find=${query}`; // Redirect to the search view with the query
    //   }
    // });

});