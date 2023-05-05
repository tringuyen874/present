//get selected algorithm
function getAlgo() {
    algo = document.getElementById("get-algo").value;
    return algo;
}

// function for changing specific bar color filtering with data
function changeBarColor(d, color) {
    var smi = heightScale(d);
    svg.selectAll("rect").each(function(d, i) {
        if (smi == d3.select(this).attr("height")) {
            d3.select(this).style("fill", color);
        }
    });
}

// function for generating random data
function randomData(max, range) {
    data = [];
    n = 0;
    while (n < max) {
        d = Math.floor(Math.random() * range) + 1;
        if (data.includes(d) != true) {
            data.push(d);
            n++;
        }
    }
    data.sort((a, b) => a - b);
    return data;
}

//function for creating chart.
function createChart(data) {
    svg = d3.select("#chart").append("svg");

    bandScale = d3.scaleBand().domain(data).range([0, areaWidth]).padding(0.1);

    svg.attr("width", areaWidth).attr("height", areaHeight);

    svg
        .selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return bandScale(d);
        })
        .attr("y", function(d) {
            return areaHeight - heightScale(d);
        })
        .attr("width", function() {
            return bandScale.bandwidth();
        })
        .attr("height", function(d) {
            return heightScale(d);
        })
        .style("fill", "rgb(173, 216, 230)");

    svg
        .selectAll("text")
        .data(data)
        .enter()
        .append("text")
        .text(function(d) {
            return d;
        })
        .attr("x", function(d, i) {
            return bandScale(d) + 10;
        })
        .attr("y", function(d) {
            return areaHeight - 15;
        })
        .style("width", bandScale.bandwidth())
        .style("fill", "black")
        .style("font-size", areaWidth / data.length / 3)
        .style("font-family", "sans-serif")
        .style("z-index", 1);
}