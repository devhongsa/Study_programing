import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.CacheManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.connection.RedisStandaloneConfiguration;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.StringRedisSerializer;


@RequiredArgsConstructor
@Configuration
public class CacheConfig {

    @Value("${spring.redis.host}")
    private String host;

    @Value("${spring.redis.port}")
    private int port;

    @Bean
    public CacheManager redisCacheManager(RedisConnectionFactory redisConnectionFactory) {
        RedisCacheConfiguration conf = RedisCacheConfiguration.defaultCacheConfig()
                // .disableCachingNullvalues() // null값이 redis에 저장되는것을 방지
                // .computePrefixWith(CacheKeyPrefix.simple()) //Cache에 저장될때 key값앞에 Prefix에 대한 내용 
                .serializeKeysWith(
                        RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
                .serializeValuesWith(RedisSerializationContext.SerializationPair
                        .fromSerializer(new GenericJackson2JsonRedisSerializer()));
        // .entryTtl(Duration.ofSeconds(10)) cache데이터의 유효기간을 설정할 수 있음.

        // 특정 캐시에 대한 TTL 설정
        HashMap<String, RedisCacheConfiguration> configMap = new HashMap<>();
        configMap.put("CacheName", RedisCacheConfiguration.defaultCacheConfig()
                .entryTtl(Duration.ofSeconds(5)));

        return RedisCacheManager.RedisCacheManagerBuilder.fromConnectionFactory(redisConnectionFactory)
                .cacheDefaults(conf)
                // .withInitialCacheConfiguration(configMap)
                .build();
    }

    @Bean
    public RedisConnectionFactory redisConnectionFactory() {
        //sentinel 구성시
        RedisSentinelConfiguration redisSentinelConfiguration = new RedisSentinelConfiguration()
                .master("mymaster") 
                .sentinel("sentinel IP",5000)
                .sentinel("sentinel IP2",5001)
                .sentinel("sentinel IP3",5002);
        return LettuceConnectionFactory(redisSentinelConfiguration);

        // RedisClusterConfiguration : cluster로 구성할땐 이걸로

        // standalone 
        RedisStandaloneConfiguration conf = new RedisStandaloneConfiguration();
        conf.setHostName(host);
        conf.setPort(port);
        // conf.setPassword();
        return new LettuceConnectionFactory(conf);
    }


    // redisTemplate 사용시 설정 
    @Bean
    public RedisTemplate<String, Object> redisTemplate() {
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory());
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(new StringRedisSerializer());
        return redisTemplate;
    }

    
    // redis pub-sub 사용시 설정
    @Bean
    RedisMessageListenerContainer redisContainer() {
        final RedisMessageListenerContainer container = new RedisMessageListenerContainer();
        container.setConnectionFactory(redisConnectionFactory());
        return container;
    }
}