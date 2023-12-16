document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});

document.addEventListener("DOMContentLoaded", function () {
    // navbar and logo
    let navbar = document.querySelector("nav");
    let logo = document.querySelector(".brand-logo img");

    // Set the navbar height to the logo height
    navbar.style.height = logo.offsetHeight + "px";
});

document.addEventListener('DOMContentLoaded', function () {
    // data picker
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker);
});

document.addEventListener('DOMContentLoaded', function () {
    // category picker
    let categoryPicker = document.querySelectorAll('select');
    M.FormSelect.init(categoryPicker);
});