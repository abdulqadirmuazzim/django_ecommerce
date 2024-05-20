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

