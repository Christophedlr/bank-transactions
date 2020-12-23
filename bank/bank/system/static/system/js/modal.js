$.each($('[data-toggle="modal"]'), function() {
    target = $(this).data('target');

    if ($(target).hasClass("modal")) {
        $(target).dialog({
            autoOpen: false,
            modal: true
        });
        $('.ui-dialog-titlebar').remove();

        $(target).find('[data-dismiss="modal"]').on('click', function() {
            $('.modal').dialog('close');
        });
    }
});

$('[data-toggle="modal"]').button().on("click", function() {
    $($(this).data('target')).dialog("open");
});
