PIE = document.getElementById('pieplot');

var data = [{
    labels: ['Jawa Timur', 'Jawa Tengah', 'Jawa Barat', 'Sulawesi Selatan', 'Sumatera Selatan', 'Lampung', 'Sumatera Utara', 'Aceh', 'Banten', 'Sumatera Barat', 'Provinsi Lainnya'],
    values: [17.361560447636606, 16.777444921103285, 16.39600523783789, 9.007528369725966, 5.202780793410973, 4.675654370487766, 4.320901146301643, 3.067236649300317, 2.9684821889164064, 2.7587708817993053, 17.463634993479857],
    type: 'pie'
}];

var layout = {
    title: 'Kontribusi Produksi Padi<br><span style="font-size:0.5em;color:gray">Rata-rata tahun 2017 hingga 2022</span>',
    font: {size: 13},
    margin: {t: 100, b: 50, l: 70, r: 70},

};

var config = {responsive: true};
Plotly.newPlot(PIE, data, layout, config);