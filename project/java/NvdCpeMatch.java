package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A CPE match string or range, and whether what it matches is vulnerable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCpeMatch  {

  private String criteria;
  private String matchCriteriaId;
  private String versionStartExcluding;
  private String versionStartIncluding;
  private String versionEndExcluding;
  private String versionEndIncluding;
  private boolean vulnerable;


}