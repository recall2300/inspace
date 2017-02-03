var inbee = window.inbee || {};
inbee.basic = inbee.basic || {};
//inbee.basic.sidebar = {};
inbee.basic.ready = function () {
    $('.ui.labeled.icon.sidebar')
        .sidebar('setting', 'transition', 'overlay')
        .sidebar('attach events', '.menu .icon')
    ;
    $('.ui.dropdown')
        .dropdown()
    ;
    $('.approval-line-modal').modal({
        allowMultiple: true
    });
    $('.modal-form.modal')
        .modal('attach events', '.showmodal.button', 'show')
    ;
    $('.approval-line-modal.info').each(function (idx, elem) {
        $(elem).modal('attach events', '#' + $(elem).attr('data-object'));
    });

}

// attach ready event
$(document)
    .ready(inbee.basic.ready)
;
