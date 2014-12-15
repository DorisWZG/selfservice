function check_submit() {
    var category = $("#selectCategory").val();
    var budget = $("#selectBudget").val();
    var resultButton = $("#see_result_button");
    if (budget != "" && category != "") {
        resultButton.removeClass('disabled');
    } else {
        resultButton.addClass("disabled");
    }
}

function showResult() {
    $("#submit").attr('disabled','disabled');
    var category = $("#selectCategory").val();
    var budget = $("#selectBudget").val();
    var url = "/budget_allocation/metrics_result/industry/" + category + "/budget/" + budget;
    $.get(url).done(function(data) {
        var table = $("#result-table");
        table.find("tr").slice(1).remove();
        table.addClass("hidden");
        $(data).each(function(idx, value) {
            var row = $("<tr></tr>");
            $("<td></td>").html(value["channelName"]).appendTo(row);
            $("<td></td>").html(value["allocation"]).appendTo(row);
            $("<td></td>").html(value["expectedClicks"]).appendTo(row);
            $("<td></td>").html(value["costPerClick"]).appendTo(row);
            $("<td></td>").html(value["expectedImpressions"]).appendTo(row);
            $("<td></td>").html(value["costPerImpression"]).appendTo(row);
            row.appendTo(table);
        });
        table.removeClass("hidden");
    }).fail(function(data) {
        alert("Status Code: " + data.status + ", Status Text: " + data.statusText + ", Response Text: " + data.responseText);
    });

}

function showResultPage() {
    var category = $("#selectCategory").val();
    var budget = $("#selectBudget").val();
    if (category == "") {
        alert("Please choose a category");
        return;
    }
    if (budget == "") {
        alert("Please choose a budget");
        return;
    }
    window.location = "/stage2_result/industry/" + category + "/budget/" + budget;
}
//$.ajax({
//        url: siteUrl + "/restapi/industry_list",
//        method: "GET",
//        headers: { "Accept": "application/json; odata=verbose" },
//        success: function (data) {
//           console.log(JSON.stringify(data.d.results));
//        },
//        error: function (data) {
//           console.log(JSON.stringify(data));
//        }
//});