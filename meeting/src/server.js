const app = require('./app');
const { Eureka } = require('eureka-js-client');

// Port lu depuis la variable d'environnement PORT (8083 par défaut)
const PORT = Number(process.env.PORT) || 8083;
const BASE_URL = `http://localhost:${PORT}`;

// Configuration du client Eureka
const eurekaClient = new Eureka({
  instance: {
    app: 'MEETING',
    instanceId: `localhost:meeting:${PORT}`,
    hostName: 'localhost',
    ipAddr: '127.0.0.1',
    port: {
      $: PORT,
      '@enabled': true,
    },
    vipAddress: 'meeting',
    homePageUrl: `${BASE_URL}/`,
    statusPageUrl: `${BASE_URL}/info`,
    healthCheckUrl: `${BASE_URL}/health`,
    dataCenterInfo: {
      '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
      name: 'MyOwn',
    },
  },
  eureka: {
    host: 'localhost',
    port: 8761,
    servicePath: '/eureka/apps/',
  },
});

app.listen(PORT, () => {
  console.log(`meeting microservice running on ${BASE_URL}`);
  console.log(`Swagger UI: ${BASE_URL}/swagger-ui`);
  console.log(`Health: ${BASE_URL}/health  |  Info: ${BASE_URL}/info`);

  // Enregistrement dans Eureka au démarrage
  eurekaClient.start((error) => {
    if (error) {
      console.error('Eureka registration failed:', error);
    } else {
      console.log('Registered in Eureka as MEETING');
    }
  });
});

// Désinscription propre d'Eureka à l'arrêt (Ctrl + C)
process.on('SIGINT', () => {
  eurekaClient.stop(() => process.exit(0));
});