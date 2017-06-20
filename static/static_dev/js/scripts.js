$(document).ready(function(){
    var form = $('#settings_form');
    console.log(form);

        function cartUpdating(product_id, nmb, is_delete, winding, veins, coil) {
            var data = {};
            data.is_delete = is_delete;
            data.product_id = product_id;
            data.winding = winding;
            data.veins = veins;
            data.coil = coil;
            data.nmb = nmb;
            var csrf_token = $('#cart_form [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            var url = /cart_adding/;
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                     if(is_delete){
                        data.is_delete = true;
                        console.log("is_delete = ", is_delete);
                        console.log("csrf-delete = ", csrf_token);
                        console.log("data.is_delete = ", data.is_delete)
                     }
                     else{
                        console.log("is_delete = ", is_delete);
                        console.log("csrf-add = ", csrf_token);
                     }
                    console.log("prod tot nmb = ", data.products_total_nmb);
                    if (data.products_total_nmb || data.products_total_nmb == 0) {
                        $('#cart_total_nmb').text(data.products_total_nmb);
                        console.log(data.products);
                        $('.cart_table_row').html("");
                        $.each(data.products, function (k, v) {
                            v.price = v.nmb * v.price;
                            $('.cart_table_row').append('<li><div class="cart_item"><div class="cart_name">' + v.name + '</div>' +
                                '<div class="cart_nmb">Кол-во: ' + v.nmb + '</div>' +
                                '<div class="cart_item_price total_item_price_header" id="total_item_price_header">' +
                                ' ' + v.price + ' Rub</div>' +
                                '<div> <a class="delete_item" href="#" data-product_id="' + v.id + '">X</a></div></div></li>');
                        });
                        console.log("ok");
                    }
                },
                error: function () {
                    console.log("error");
                }
            });

        }

    form.on('submit', function(e) {
        e.preventDefault();
        var veins = $("#settings_form input:radio[name = veins]:checked").val();
        console.log(veins);
        var winding = $("#settings_form input:radio[name = winding]:checked").val();
        console.log(winding);
        var coil = $('#coil ').val();
        console.log(coil);
        var nmb = $('#nmb').val();
        console.log(nmb);
        var buy_button = $("#buy_button");
        var product_id = buy_button.data("product_id");
        console.log(product_id);
        var product_name = buy_button.data("product_name");
        console.log(product_name);
        var product_price = buy_button.data("product_price") * nmb;
        console.log(product_price);
        var is_delete = false;
        cartUpdating(product_id, nmb, is_delete, winding, veins, coil);
    });



    $(document).on('click', '.delete_item', function(e){
         e.preventDefault();
         var product_id = $(this).data("product_id");
         var nmb = 0;
         var is_delete = true;
         cartUpdating(product_id, nmb, is_delete , 0 , 0, 0);
         $('#total_item_price_header').change();

     });


    function calculatingCartAmount() {
        var checkout_price = 0;
        $('.total_item_price').each(function () {
            checkout_price = checkout_price + parseInt($(this).text());
        });
        $('#checkout_price').text(checkout_price);
    }


    function calculatingCartAmountHeader() {
        var checkout_price = 0;
        $('.total_item_price_header').each(function () {
            checkout_price = checkout_price + parseInt($(this).text());
        });
        $('#checkout_price_header').text(checkout_price);
    }


    $('.cart').mouseenter(function () {
        calculatingCartAmountHeader();
    });


    calculatingCartAmountHeader();
    calculatingCartAmount();
});




