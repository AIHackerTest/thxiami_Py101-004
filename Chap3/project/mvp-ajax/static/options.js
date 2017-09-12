var default_option = {
        title : {
            text: '未来5天气温变化',
           	x:'center',
            textStyle: {
                 fontSize: 20,
                  color: '#333'
            }
        },
        // tooltip : {
        //     trigger: 'axis'
        // },
        legend: {
            data:['最高气温','最低气温'],
           	x:'right',
        },
        xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : ['周一','周二','周三','周四','周五']
        }
        ],
        yAxis : [
        {
            type : 'value',
            boundaryGap : [0, 0.2],
            axisLabel : {
                formatter: '{value} °C'
            }
        }
        ],
        series : [
        {
            name:'最高气温',
            type:'line',
            data:[11, 11, 15, 13, 12],
            markPoint : {
                data : [
                    {name: '周一', value: 11, xAxis: 0, yAxis: 11},
                    {name: '周二', value: 11, xAxis: 1, yAxis: 11},
                ],
              symbolSize: 18,
               itemStyle: {
                    normal: {
                       label:{
                         formatter: '{c} °C '
                       }
                    }
               }
            }
        },
        {
            name:'最低气温',
            type:'line',
            data:[1, -2, 2, 5, 3],
            markPoint : {
                data : [
                    {name : '周最低', value : -2, xAxis: 1, yAxis: -1.5}
                ],
                symbolSize: 18,
                itemStyle: {
                    normal: {
                       label:{
                         formatter: '{c} °C '
                       }
                   }
               }
            },
        }
        ]
};