$(document).ready(function() {

    var map = L.map('map').setView([40.712216, -74.22655], 13);
    var imageUrl = 'https://s3.amazonaws.com/uploads.hipchat.com/466087/2978340/1nc1yFkOs8gkHmS/Kyiv1%20poverh%202-3-page-001.jpg',
    //var imageUrl = '/static/floor2.jpg',
    imageBounds = [[40.712216, -74.22655], [40.803941, -74.12544]];

    L.imageOverlay(imageUrl, imageBounds).addTo(map);


    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);

    var drawControl = new L.Control.Draw({
        draw: {
            position: 'topleft',
            polygon: {
                title: 'Draw a sexy polygon!',
                allowIntersection: false,
                drawError: {
                    color: '#b00b00',
                    timeout: 1000
                },
                shapeOptions: {
                    color: '#bada55'
                },
                showArea: true
            },
            polyline: {
                metric: false
            },
            circle: {
                shapeOptions: {
                    color: '#662d91'
                }
            }
        },
        edit: {
            featureGroup: drawnItems
        }
    });
    map.addControl(drawControl);

    map.on('draw:created', function (e) {
        var type = e.layerType,
            layer = e.layer;

        if (type === 'marker') {
            layer.bindPopup('A popup!');
        }

        drawnItems.addLayer(layer);
    });

    map.on('draw:created', function (e) {
        var type = e.layerType;
        var layer = e.layer;

        var shape = layer.toGeoJSON()
        var shape_for_db = JSON.stringify(shape);
        alert(shape_for_db);
    });


})