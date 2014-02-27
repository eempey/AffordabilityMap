	

	var svg = d3.select("body").append("svg")
    .attr("width", 500)
    .attr("height", 300);

	var projection = d3.geo.albers()
	    .scale(20000)
	    .translate([500 / 2, 300 / 2]);



	var path = d3.geo.path()
	    .projection(projection);


	d3.json('census-tracts-2011.json', function(json){
		svg.selectAll("path")
			.data(json.features)
			.enter()
			.append("path")
			.attr("d",path);
			});
	