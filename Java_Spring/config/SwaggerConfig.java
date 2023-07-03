@Configuration
@EnableSwagger2
public class SwaggerConfig {

    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                //.apis(RequestHandlerSelectors.any()) // basic-error-controller 까지 swagger에 나오게됨.
                .apis(RequestHandlerSelectors.basePackage("com.zbhong.weather"))
                .paths(PathSelectors.any())
                //.paths(PathSelectors.ant("/read/**")) // /read path에 있는 모든 mapping들만 swagger에 게시
                .build().apiInfo(apiInfo());
    }

    private ApiInfo apiInfo() {
        String description = "Welcome Log Company";
        return new ApiInfoBuilder()
                .title("SWAGGER TEST")
                .description(description)
                .version("1.0")
                .build();
    }

}