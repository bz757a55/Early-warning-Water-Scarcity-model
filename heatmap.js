const districtData = {
  "ariyalur": 46.89,
  "chengalpattu": 67.88,
  "chennai": 133,
  "coimbatore": 84.45,
  "cuddalore": 75.86,
  "dharmapuri": 111.77,
  "dindigul": 131.77,
  "erode": 82.36,
  "kallakkurichi": 71.4,
  "kancheepuram": 51.96,
  "kanniyakumari": 16.9,
  "karur": 95.73,
  "krishnagiri": 97.71,
  "madurai": 72,
  "nagapattinam": 136.78,
  "namakkal": 116.15,
  "perambalur": 113.39,
  "pudukkottai": 44.71,
  "ramanathapuram": 8.46,
  "ranipet": 90.91,
  "sivaganga": 27.37,
  "tenkasi": 80.02,
  "thanjavur": 99.97,
  "the nilgiris": 9.3,
  "theni": 76.56,
  "thiruvallur": 55.2,
  "thiruvarur": 80.63,
  "thoothukkudi": 35.81,
  "tiruchirappalli": 78.38,
  "tirunelveli": 45.79,
  "tirupathur": 147.34,
  "tiruppur": 85.85,
  "tiruvannamalai": 82.38,
  "vellore": 115.06,
  "viluppuram": 89.52,
  "virudhunagar": 57.56,
  "salem": 125.85
};

const svg = document.getElementById("map");
const dataInfo = document.getElementById("data-info");
const loadingText = document.getElementById("loading");

function getColor(value) {
  const max = Math.max(...Object.values(districtData));
  const min = Math.min(...Object.values(districtData));
  const range = max - min;
  const percent = (value - min) / range;
  const colorScale = d3.scaleLinear()
    .domain([0, 1])
    .range(["lightgreen", "darkred"]);
  return colorScale(percent);
}


function drawDistrict(feature) {
  const path = d3.geoPath().projection(projection)(feature);
  svg.append("path")
    .attr("d", path)
    .attr("fill", getColor(districtData[feature.properties.district]))
    .attr("stroke", "black")
    .attr("stroke-width", 1)
    .on("mouseover", () => {
      dataInfo.innerHTML = `<b>${feature.properties.district}:</b> ${districtData[feature.properties.district]}`;
    })
    .on("mouseout", () => {
      dataInfo.innerHTML = "";
    });
}


const width = 600;
const height = 400;
const projection = d3.geoAlbers()
  .scale(1200)
  .translate([width / 2, height / 2]);


d3.json("C:/Users/adars/OneDrive/Desktop/temp/TamilNadu.geojson", (geoData) => {
  loadingText.innerHTML = "";
  geoData.features.forEach(drawDistrict);
});


d3.json("C:/Users/adars/OneDrive/Desktop/temp/TamilNadu.geojson", (geoData, error) => {
  if (error) {
    console.error("Error fetching GeoJSON data:", error);
    loadingText.innerHTML = "Error loading data";
  } else {
    // ... existing success handler code
  }
});
