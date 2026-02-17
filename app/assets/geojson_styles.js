// assets/my_logic.js
window.dashExtensions = Object.assign({}, window.dashExtensions, {
    my_namespace: {
        lake_style: function(feature) {
            const d = feature.properties['Lake Type'];
            
            // Map your classes to colors
            const colors = {
                1: "#00B0F0",
                2: "#92D050",
                3: "#FFFF00",
                4: "#FF0000"
            };
			
			const line_colors = {
                1: "#0099D1",
                2: "#82C936",
                3: "#D1D100",
                4: "#D10000"
            };

            return {
                fillColor: colors[d] || "#808080", // Default to gray if type missing
                weight: 2,
                opacity: 1,
                color: line_colors[d] || "#808080",
                fillOpacity: 0.7
            };
        }
    }
});