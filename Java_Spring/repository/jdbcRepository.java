package Java_Spring.repository;

// JDBC repository는 class로 만들고 JPA는 interface로 만든다
@Repository
public class JdbcMemoRepository {
    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public JdbcMemoRepository(DataSource dataSource) {
        jdbcTemplate = new JdbcTemplate(dataSource);
    }

    public Memo save(Memo memo) {
        String sql = "insert into memo values(?,?);";
        jdbcTemplate.update(sql, memo.getId(), memo.getText());
        return memo;
    }

    public List<Memo> findAll() {
        String sql = "select * from memo;";
        return jdbcTemplate.query(sql, memoRowMapper());
    }

    public Optional<Memo> findById(int id) {
        String sql = "select * from memo where id=?;";
        return jdbcTemplate.query(sql, memoRowMapper(), id).stream().findFirst();
        // stream findFirst 한 이유는 query의 ResultSet은 리스트 형태로 리턴하게 되어있기 때문.
        // id로 find하면 값이 하나일거라는 걸 알기때문에 단일 객체로 리턴하게 해주려고
    }

    private RowMapper<Memo> memoRowMapper() {
        return (rs, rowNum) -> new Memo(
                rs.getInt("id"),
                rs.getString("text"));
    }
}