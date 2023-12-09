document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});

document.addEventListener("DOMContentLoaded", function () {
    var navbar = document.querySelector("nav");
    var logo = document.querySelector(".brand-logo img");

    // Set the navbar height to the logo height
    navbar.style.height = logo.offsetHeight + "px";
});

document.addEventListener('DOMContentLoaded', function () {
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker);
});