function bindCatSelection(divElem) {
    divElem.find('ul.dropdown-menu li').click(function() {
        var parentDiv = $(this).parent().parent();
        parentDiv.find('button strong').text($(this).children('a').text());
        var selectedCatId = $(this).children('span.hidden').text();
        parentDiv.children('input[type="text"]').val(selectedCatId);
        var nextDiv = parentDiv.next('div');
        if (nextDiv.length) {
            fillNextCat(nextDiv, parentDiv.children('img').prop('name'), selectedCatId);
        }
    });
    var reqVal = divElem.children('label.hidden').text();
    if (reqVal != '') {
        reqLi = divElem.find('li').filter(function() {
            return $(this).children('span.hidden').text() == reqVal;
        });
        if (reqLi.length > 0) {
            reqLi.click();
        }
    }
}

function fillNextCat(nextDiv, api, catId) {
    $.get('/member_service/' + api + '/' + catId).done(function(data) {
        var ulElem = nextDiv.children('ul');
        ulElem.children().slice(1).remove();
        if (data.length > 0) {
            $(data).each(function (idx, item) {
                $('<li><span class="hidden">' + item['id'] + '</span><a>' + item['eng_kw'] + '</a></li>').appendTo(ulElem);
            });
            nextDiv.children('button').removeClass('disabled');
        }
        bindCatSelection(nextDiv);
        if (data.length == 0) {
            ulElem.children().first().click();
            nextDiv.children('button').addClass('disabled');
        }
    });
}

function createTrendChart(summary_div, divs, titles, names, datum, colorIndices) {
    summary_div.children().remove();
    summary_div.highcharts('StockChart', createChartDict('Indices Trends Summary', names, datum, colorIndices));
    summary_div.highcharts().reflow();
    for (var i = 0; i < divs.length; i++) {
        var div = divs[i];
        div.children().remove();
        div.highcharts('StockChart', createChartDict(titles[i], [names[i]], [datum[i]], [colorIndices[i]]));
        div.highcharts().reflow();
    }
}

function createChartDict(title, names, datum, colorIndices) {
    var chartDict = {
        title: { text: title },
        rangeSelector: { selected: 1 },
        yAxis: { minRange: 0 },
        series: []
    };
    for (var i = 0; i < names.length; i++) {
        var color = Highcharts.getOptions().colors[colorIndices[i]];
        var seriesOptions = {
            name: names[i],
            data: datum[i],
            color: color
        };
        if (names.length == 1) {
            seriesOptions.type = 'area';
            seriesOptions.fillColor = {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [ [0, color], [1, Highcharts.Color(color).setOpacity(0).get('rgba')] ]
            };
            chartDict.navigator = {
                series: { lineColor: color }
            };
        }
        chartDict.series.push(seriesOptions);
    }
    chartDict.plotOptions = {
        line: { shadow: true }
    };
    return chartDict;
}