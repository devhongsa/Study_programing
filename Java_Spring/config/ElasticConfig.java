
@Configuration
public class ElasticsearchConfig extends AbstractElasticsearchConfiguration {

    @Value("${ELASTICSEARCH.HOST}")
    private String host;  // 127.0.0.1:9200,127.0.0.2:9200

    @Override
    public ElasticsearchOperations elasticsearchOperations(ElasticsearchConverter elasticsearchConverter, RestHighLevelClient elasticsearchClient) {
        return new ElasticsearchRestTemplate(elasticsearchClient());
    }

    @Override
    public RestHighLevelClient elasticsearchClient() {
        ClientConfiguration clientConfiguration = ClientConfiguration.builder()
                .connectedTo(host.split(","))
                .build();
        return RestClients.create(clientConfiguration).rest();
    }
}






@Configuration
public class ElasticConfig extends ElasticsearchConfiguration {

    @Value("${spring.elasticsearch.uris}")
    private String elasticUrl;

    @Override
    @Bean
    public ClientConfiguration clientConfiguration() {
        return ClientConfiguration.builder()
                .connectedTo(elasticUrl)
                .build();
    }
}