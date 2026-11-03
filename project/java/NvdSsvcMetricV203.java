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
  A Stakeholder-Specific Vulnerability Categorization (SSVC) decision and who made it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdSsvcMetricV203  {

  private String source;
  private NvdSsvcData ssvcData;


}