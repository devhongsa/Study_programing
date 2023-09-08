
package com.dokkebi.officefinder.security;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.autoconfigure.security.servlet.PathRequest;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;


@Slf4j
@Configuration
@EnableWebSecurity(debug = true)
@EnableGlobalMethodSecurity(prePostEnabled = true)
@RequiredArgsConstructor
public class SecurityConfig implements WebMvcConfigurer {

  /*
      client에서 요청을 날리면 Spring Security의 여러 filterChain 들을 거치게 됨.
      그 체인들에 대한 설정을 하는 Bean 임.
      disable()로 특정 필터를 거치지않게 할 수 있음.
   */

  private final TokenProvider tokenProvider;
  public static final String ALLOWED_METHOD_NAMES = "GET,HEAD,POST,PUT,DELETE,TRACE,OPTIONS,PATCH";



  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .httpBasic().disable()
        .csrf().disable()
        .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        .and()
        .authorizeHttpRequests((authz) -> authz
            .antMatchers("/ws/**").permitAll() // 개발환경에서만 우선 설정
            .antMatchers("/webjars/**").permitAll() // 개발환경에서만 우선 설정
            .antMatchers("/swagger*/**","/v3/api-docs", "/v2/api-docs").permitAll()
            .antMatchers("/**/signup", "/**/login/**").permitAll()
            .anyRequest().authenticated()
        )
        .addFilterBefore(new JwtAuthenticationFilter(tokenProvider), UsernamePasswordAuthenticationFilter.class);
    return http.build();
  }

  @Bean
  public WebSecurityCustomizer webSecurityCustomizer() {
    return (web) -> web.ignoring()
        //.antMatchers("/ignore1", "/ignore2")
        .requestMatchers(PathRequest.toStaticResources().atCommonLocations());
  }


  // Cors 에러 관련 설정 
  @Override
  public void addCorsMappings(CorsRegistry registry) {
    registry.addMapping("/**")
        .allowedOrigins("http://127.0.0.1:5173", "http://localhost:5173")
        .allowedMethods("*") // GET, POST, PUT, DELETE ... 등 모두 허용
        .allowedHeaders("*") // 모든 헤더 허용
        .exposedHeaders("..") // 프론트에서 응답 헤더 내용 사용가능하게 하는 기능 
        .allowCredentials(true); // 쿠키 허용 여부
  }
}




