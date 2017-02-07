var inbee = window.inbee || {};
inbee.basic = inbee.basic || {};
//inbee.basic.sidebar = {};
inbee.basic.ready = function () {
    var calendarFormatter = {
        date: function (date, settings) {
            if (!date) return '';
            var day = date.getDate();
            var month = date.getMonth() + 1;
            var year = date.getFullYear();
            return year + '-' + month + '-' + day;
        }
    };
    var today = new Date();
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

    $('.calendar-init-date').val(today);
    $('#rangestart').calendar({
        monthFirst: false,
        type: 'date',
        formatter: calendarFormatter,
        endCalendar: $('#rangeend'),
        onChange: function (date, text) {
            var startDate = date;
            var endDate = $('#rangeend').calendar('get date');
            var dateDiffToDay = Math.abs((startDate - endDate) / 1000 / 60 / 60 / 24) + 1;
            $('#id_leave_day').val(dateDiffToDay);
        }
    });
    $('#rangeend').calendar({
        monthFirst: false,
        type: 'date',
        formatter: calendarFormatter,
        startCalendar: $('#rangestart'),
        onChange: function (date, text) {
            var startDate = $('#rangestart').calendar('get date');
            var endDate = date;
            var dateDiffToDay = Math.abs((startDate - endDate) / 1000 / 60 / 60 / 24) + 1;
            $('#id_leave_day').val(dateDiffToDay);
        }
    });
}

$(document)
    .ready(inbee.basic.ready)
;
