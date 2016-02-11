
function setup_rate_chart(container_name, description, data) {
    var cont = $('#' + container_name);
    console.log(['data', data]);
    var hc = cont.highcharts({
        title: {
            text: 'Tracking sleep for ' + description,
	    style: {
                    fontSize: '26px'
                }
        },

        subtitle: {
            //text: 'this is a subtitle'
        },
	chart: {
            zoomType: 'x',
	    spacingRight: 50,
	    //marginTop: 75
        },
        xAxis: {
	    title: {
		text: 'Days'
		},
            tickInterval: 7,
            tickWidth: 0,
            gridLineWidth: 1,
            labels: {
                align: 'left',
                x: 3,
                y: -3
            }
        },

        yAxis: [{ // left y axis
            title: {
                text: 'Event rate per night'
            },
            labels: {
                align: 'left',
                x: 3,
                y: 16,
                format: '{value:.,1f}'
            },
            showFirstLabel: false
        }, { // right y axis
            linkedTo: 0,
            gridLineWidth: 0,
            opposite: true,
            title: {
                text: null
            },
            labels: {
                align: 'right',
                x: -3,
                y: 16,
                format: '{value:.,0f}'
            },
            showFirstLabel: false
        }],

        legend: {
            align: 'left',
            //verticalAlign: 'top',
            //y: 20,
            //floating: true,
            //borderWidth: 0
	     itemStyle: {
                fontSize: '16px'
            }
	    
        },
	
        tooltip: {
            shared: true,
            crosshairs: true,
	    valueDecimals: 4,
        },

        plotOptions: {
            series: {
                cursor: 'pointer',
                marker: {
                    lineWidth: 1
                }
            }
        },

        series: [{
            name: 'Sleep Disruption',
	    data: data["rate_disr"],
            lineWidth: 4,
            marker: {
                radius: 5
            },
        }, {
            name: 'Device use/Intervention applied',
	    data: data["rate_use"],
	    lineWidth: 4,
	    marker: {
                radius: 5
            },
        }, {
            name: 'Intervention worked',
	    data: data["rate_worked"],
	    lineWidth: 4,
	    marker: {
                radius: 5
            },
        }, {
	    name: 'Initial rate of sleep distruption',
	    data: [[data["init_day"], data["init_rate"]]],
	    lineWidth: 4,
	    marker: {
                radius: 7
            },
	}]
    });
    console.log(hc);
}
