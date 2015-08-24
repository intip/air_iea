(function ($) {
    $(function () {
        $("#id_air_file").change(function () {
            if (! confirm("Deseja mesmo carregar outro arquivo AIR ?")) {
                this.value = '';
            };
        });
    });
})(django.jQuery);
