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
  A CPE match string or range as NVD holds it, and the CPE names it matches.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdMatchString  {

  private String criteria;
  private String matchCriteriaId;
  private String versionStartExcluding;
  private String versionStartIncluding;
  private String versionEndExcluding;
  private String versionEndIncluding;
  private ZonedDateTime created;
  private ZonedDateTime lastModified;
  private String status;
  private ZonedDateTime cpeLastModified;
  private List<NvdMatchedCpe> matches;


}