var randomScalingFactor = function() {
  return Math.round(Math.random() * 100);
};

var config = {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [
        randomScalingFactor(),
        randomScalingFactor(),
      ],
      backgroundColor: [
        window.chartColors.orange,
        window.chartColors.yellow,
      ],
      label: 'Dataset 1',
      borderWidth : 0
    }],
    labels: [
      "Orange",
      "Yellow",
    ]
  },
  options: {
    cutoutPercentage: 88,
    responsive: true,
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Chart.js Doughnut Chart'
    },
    animation: {
      animateScale: true,
      animateRotate: true
    }
  }

};

window.onload = function() {
  var i = 0;
  for (i = 0; i < 2; i++) {
    var ctx = document.getElementById("chart-area" + i).getContext("2d");
    window.myDoughnut = new Chart(ctx, config);
  }
};
