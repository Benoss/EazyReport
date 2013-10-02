<script >
$(function () {
    $.get('{{content.data_json}}', function (json_data) {
         $('#{{content.id}}').highcharts(
         {
         chart: {
             plotBackgroundColor: null,
             plotBorderWidth: null,
             plotShadow: false
         },
         title: {
             text: '{{content.description}}'
         },
         tooltip: {
             pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
         },
         plotOptions: {
             pie: {
                 allowPointSelect: true,
                 cursor: 'pointer',
                 dataLabels: {
                     enabled: true,
                     color: '#000000',
                     connectorColor: '#000000',
                     format: '<b>{point.name}</b>: <br /> {point.percentage:.1f} % Total:{point.y}'
                 },
                 showInLegend: true,
             }
         },
         series: [{
             type: 'pie',
             name: '{{content.title}}',
             data: json_data,
         }]
         
         });
    });
});
</script >