// ================================
// Queue Length Trend
// ================================

const queueCanvas = document.getElementById("queueChart");

if (queueCanvas) {

    new Chart(queueCanvas, {

        type: "line",

        data: {

            labels: ["Waiting", "Serving", "Served", "Cancelled"],

            datasets: [{

                label: "Tokens",

                data: [

                    waiting,
                    serving,
                    served,
                    cancelled

                ],

                borderColor: "#2563eb",

                backgroundColor: "rgba(37,99,235,0.15)",

                fill: true,

                tension: 0.4,

                borderWidth: 3

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    ticks: {

                        precision: 0

                    }

                }

            }

        }

    });

}


// ================================
// Token Status Doughnut Chart
// ================================

const statusCanvas = document.getElementById("statusChart");

if (statusCanvas) {

    new Chart(statusCanvas, {

        type: "doughnut",

        data: {

            labels: [

                "Waiting",

                "Serving",

                "Served",

                "Cancelled"

            ],

            datasets: [{

                data: [

                    waiting,
                    serving,
                    served,
                    cancelled

                ],

                backgroundColor: [

                    "#f4b400",

                    "#4285f4",

                    "#34a853",

                    "#ea4335"

                ]

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "top"

                }

            }

        }

    });

}


// ================================
// Daily Served Chart
// ================================

const servedCanvas = document.getElementById("servedChart");

if (servedCanvas) {

    new Chart(servedCanvas, {

        type: "bar",

        data: {

            labels: [

                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"

            ],

            datasets: [{

                label: "Tokens Served",

                data: servedData,

                backgroundColor: "#2563eb",

                borderRadius: 8,

                borderSkipped: false

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                },

                tooltip: {

                    callbacks: {

                        label: function(context) {

                            return context.raw + " Tokens";

                        }

                    }

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    ticks: {

                        precision: 0,

                        stepSize: 1

                    },

                    title: {

                        display: true,

                        text: "Tokens"

                    }

                },

                x: {

                    title: {

                        display: true,

                        text: "Days"

                    }

                }

            }

        }

    });

}