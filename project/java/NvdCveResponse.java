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
  A page of the vulnerability API's results, or a whole data feed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCveResponse  {

  private List<NvdVulnerability> vulnerabilities;
  private String format;
  private ZonedDateTime timestamp;
  private int resultsPerPage;
  private int startIndex;
  private int totalResults;
  private String version;


}