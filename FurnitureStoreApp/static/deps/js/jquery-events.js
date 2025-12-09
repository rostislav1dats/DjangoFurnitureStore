// Коли html документ готовий 
$(document).ready(function () {
    // Використовуємо елемент по id - сповіщення від Django
    var notification = $('#notification');
    // І через 7 секунд видаляємо
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // По кліку на значок кошику відкриваємо модальне вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Івент клік по кнопці закрити вікно
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обробка івенту кліку радіокнопки вибору способу доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Ховаємо або відображаємо input адреси доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});