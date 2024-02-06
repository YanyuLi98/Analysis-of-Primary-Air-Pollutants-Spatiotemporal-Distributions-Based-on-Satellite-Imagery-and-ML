var Points1 = ee.FeatureCollection("")
var data1='2022-01-01';
var data2='2023-01-01';
print(Points1);
//var imageCollection = ee.ImageCollection("LANDSAT/LC08/C02/T1")
//var imageCollection = ee.ImageCollection("MODIS/061/MOD13A2")
var imageCollection = ee.ImageCollection("MODIS/061/MOD09GA")
//var imageCollection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
.filterDate(data1, data2).filterBounds(Points1)
var ft = ee.FeatureCollection(ee.List([]))

var fill = function(img, ini) {
  var inift = ee.FeatureCollection(ini)
  var ft2 = img.sampleRegions({
  collection: Points1,});
  var date = img.date().format()

  // writes the date in each feature
  var ft3 = ft2.map(function(f){return f.set("date", date)})

  // merges the FeatureCollections
  return inift.merge(ft3)
}
var newft = ee.FeatureCollection(imageCollection.iterate(fill, ft))
print(newft);
// Export
Export.table.toDrive(newft,data2,data2)
