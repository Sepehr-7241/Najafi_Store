const showSwal = document.getElementById('ShowSwal');

showSwal.addEventListener('click', function () {
    Swal.fire({
        title: "خروج از حساب کاربری با موفقیت انجام شد",
        icon: "success"
    });
})